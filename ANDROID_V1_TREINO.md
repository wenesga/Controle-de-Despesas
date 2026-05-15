# TreinoMusculacao Android V1 (Kotlin)

Este documento transforma a lógica do seu projeto Tasker em um app Android V1.

## 1) Escopo funcional (V1)

- Executar rotina de treino em dias úteis às **05:49**.
- Executar rotina de fim de semana às **06:00**.
- Executar rotina de feriado às **06:00**.
- Manter estado persistido (equivalente às variáveis globais do Tasker).
- Exibir notificação diária com ações rápidas:
  - **Exercício** (ajustar treino)
  - **Período** (editar período)
  - **Divisão** (trocar divisão)

## 2) Arquitetura sugerida

- **UI:** Jetpack Compose
- **Persistência:** DataStore (Preferences)
- **Agendamento:** WorkManager + reprogramação diária
- **Notificações:** NotificationCompat + BroadcastReceiver
- **Domínio:** Regras puras em classes de serviço/use case

```text
app/
 ├─ data/
 │   ├─ TrainingStateStore.kt
 │   └─ HolidayRepository.kt
 ├─ domain/
 │   ├─ DivisionEngine.kt
 │   ├─ PeriodizationEngine.kt
 │   ├─ SymbolsEngine.kt
 │   └─ RunTrainingUseCase.kt
 ├─ worker/
 │   ├─ WeekdayTrainingWorker.kt
 │   ├─ WeekendWorker.kt
 │   └─ HolidayWorker.kt
 ├─ notification/
 │   ├─ TrainingNotificationService.kt
 │   └─ TrainingActionReceiver.kt
 └─ ui/
     ├─ HomeScreen.kt
     └─ SettingsScreen.kt
```

## 3) Modelo de estado (equivalente ao Tasker)

```kotlin
data class TrainingState(
    val divisao: Int = 3,
    val indice: Int = 0,
    val feriado: Boolean = false,
    val numPeriodo: Int = 0,
    val diaFase: Int = 0,
    val periodoLabel: String = "Repetições Curtas",
    val numRepetLabel: String = "❘ x-y ❘",
    val estado: Int = 1,
    val semanaLabel: String = "",
    val divisaoTreinoLabel: String = "",
    val divisaoCalenLabel: String = ""
)
```

## 4) Regras centrais (port 1:1)

### 4.1 Ciclo da divisão (`1T - Principal`)

```kotlin
fun nextIndice(indiceAtual: Int, divisao: Int): Int = ((indiceAtual % divisao) + 1)
```

### 4.2 Periodização de 150 dias (`5T - Periodização`)

```kotlin
fun nextPeriod(numPeriodoAtual: Int): Triple<Int, String, String> {
    val num = ((numPeriodoAtual + 1 - 1) % 150) + 1
    return when {
        num <= 30 -> Triple(num, "Repetições Curtas", "❘ 1-6 ❘")
        num <= 60 -> Triple(num - 30, "Repetições Longas", "❘ 15-20 ❘")
        else      -> Triple(num - 60, "Repetições Média", "❘ 7-12 ❘")
    }
}
```

### 4.3 Divisão dinâmica (`4T - Divisão Treino`)

```kotlin
fun trainingConfig(divisao: Int): List<String> = when (divisao) {
    3 -> listOf("🄰 ➠ Peito, Tríceps", "🄱 ➠ Costas, Bíceps", "🄲 ➠ Pernas, Ombros")
    4 -> listOf("🄰 ➠ Peito, Cárdio", "🄱 ➠ Costas, Cárdio", "🄲 ➠ Pernas", "🄳 ➠ Ombros, Cárdio")
    5 -> listOf("🄰 ➠ Peito, Cárdio", "🄱 ➠ Costas, Cárdio", "🄲 ➠ Pernas", "🄳 ➠ Ombros, Trapézio", "🄴 ➠ Braços, Cárdio")
    6 -> listOf("🄰 ➠ Peito, Cárdio", "🄱 ➠ Costas, Cárdio", "🄲 ➠ Pernas, Abdome", "🄳 ➠ Ombros, Cárdio", "🄴 ➠ Bíceps, Cárdio", "🄵 ➠ Tríceps, Cárdio")
    else -> trainingConfig(3)
}
```

## 5) Fluxo diário

1. Carrega estado do DataStore.
2. Verifica se hoje é feriado.
3. Se dia útil e não feriado, roda fluxo principal:
   - índice -> símbolos -> divisão -> periodização -> notificação.
4. Se sábado/domingo ou feriado:
   - mantém lógica de descanso/feriado e atualiza notificação.
5. Persiste novo estado.

## 6) Ações da notificação

- **Exercício:** incrementa índice e atualiza notificação.
- **Período:** abre `Activity` com input para novo valor de período.
- **Divisão:** abre `Activity` para escolher 3/4/5/6.

## 7) Inicialização e boot

- No primeiro start do app: inicializa estado padrão (equivalente ao `9T`).
- No `BOOT_COMPLETED`: reagenda workers diários.

## 8) Roadmap imediato

1. Criar módulo Android (`app`) com Compose + WorkManager.
2. Implementar `TrainingStateStore`.
3. Implementar `RunTrainingUseCase` com as regras acima.
4. Criar `TrainingNotificationService` com 3 ações.
5. Configurar workers para horários 05:49 e 06:00.

---

Se quiser, no próximo passo eu já posso gerar os arquivos base Kotlin (classes e interfaces) em estrutura pronta para abrir no Android Studio.
