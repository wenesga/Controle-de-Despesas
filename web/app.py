from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable

from flask import Flask, flash, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "dados.db"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-change-me"
    app.config["DB_PATH"] = str(DB_PATH)

    @app.get("/")
    def index():
        rows = get_all_entries(app.config["DB_PATH"])
        categories = get_categories(app.config["DB_PATH"])
        totals = get_totals(rows)
        chart_data = get_expense_by_category(app.config["DB_PATH"])
        return render_template(
            "index.html",
            rows=rows,
            categories=categories,
            totals=totals,
            chart_data=chart_data,
        )

    @app.post("/categories")
    def add_category():
        name = request.form.get("name", "").strip()
        if not name:
            flash("Informe um nome de categoria.", "error")
            return redirect(url_for("index"))

        with sqlite3.connect(app.config["DB_PATH"]) as conn:
            conn.execute("INSERT INTO Categoria (nome) VALUES (?)", (name,))
            conn.commit()

        flash("Categoria adicionada com sucesso.", "success")
        return redirect(url_for("index"))

    @app.post("/entries")
    def add_entry():
        kind = request.form.get("kind", "").strip()
        category = request.form.get("category", "").strip()
        date = request.form.get("date", "").strip()
        amount_raw = request.form.get("amount", "").replace(",", ".").strip()

        if not kind or not date or not amount_raw:
            flash("Preencha tipo, data e valor.", "error")
            return redirect(url_for("index"))

        try:
            amount = float(amount_raw)
            if amount <= 0:
                raise ValueError
        except ValueError:
            flash("Valor inválido. Digite um número maior que zero.", "error")
            return redirect(url_for("index"))

        with sqlite3.connect(app.config["DB_PATH"]) as conn:
            if kind == "receita":
                conn.execute(
                    "INSERT INTO Receitas (categoria, adicionando_em, valor) VALUES (?, ?, ?)",
                    ("Receita", date, amount),
                )
            else:
                if not category:
                    flash("Selecione uma categoria para despesa.", "error")
                    return redirect(url_for("index"))
                conn.execute(
                    "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)",
                    (category, date, amount),
                )
            conn.commit()

        flash("Lançamento adicionado com sucesso.", "success")
        return redirect(url_for("index"))

    @app.post("/entries/<kind>/<int:entry_id>/delete")
    def delete_entry(kind: str, entry_id: int):
        table = "Receitas" if kind == "receita" else "Gastos"
        with sqlite3.connect(app.config["DB_PATH"]) as conn:
            conn.execute(f"DELETE FROM {table} WHERE id = ?", (entry_id,))
            conn.commit()

        flash("Lançamento removido.", "success")
        return redirect(url_for("index"))

    return app


def get_categories(db_path: str) -> list[str]:
    with sqlite3.connect(db_path) as conn:
        rows = conn.execute("SELECT nome FROM Categoria ORDER BY nome").fetchall()
    return [row[0] for row in rows]


def get_all_entries(db_path: str) -> list[dict]:
    with sqlite3.connect(db_path) as conn:
        expenses = conn.execute(
            "SELECT id, categoria, retirado_em AS data, valor, 'despesa' AS tipo FROM Gastos"
        ).fetchall()
        incomes = conn.execute(
            "SELECT id, categoria, adicionando_em AS data, valor, 'receita' AS tipo FROM Receitas"
        ).fetchall()

    merged = [
        {"id": rid, "categoria": cat, "data": data, "valor": float(value), "tipo": typ}
        for rid, cat, data, value, typ in [*expenses, *incomes]
    ]
    merged.sort(key=lambda x: x["data"], reverse=True)
    return merged


def get_totals(rows: Iterable[dict]) -> dict[str, float]:
    income = sum(r["valor"] for r in rows if r["tipo"] == "receita")
    expense = sum(r["valor"] for r in rows if r["tipo"] == "despesa")
    return {
        "receitas": income,
        "despesas": expense,
        "saldo": income - expense,
    }


def get_expense_by_category(db_path: str) -> dict[str, list]:
    with sqlite3.connect(db_path) as conn:
        rows = conn.execute(
            "SELECT categoria, SUM(valor) FROM Gastos GROUP BY categoria ORDER BY SUM(valor) DESC"
        ).fetchall()
    return {
        "labels": [row[0] for row in rows],
        "values": [float(row[1]) for row in rows],
    }


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
