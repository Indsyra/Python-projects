from flask import Flask, render_template, request
import csv
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

EXPENSE_FILE = "../../assets/expense_tracker/expenses.csv"
CATEGORY_FILE = "../../assets/expense_tracker/category.txt"

def load_expenses():
    return pd.read_csv(EXPENSE_FILE, names=["Date", "Category", "Amount", "Description"])


def log_expense(date, category, amount, description):
    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
  

def plot_expenses_by_category(df):
    summary = df.groupby("Category")["Amount"].sum()
    plt.figure()
    summary.plot(kind="pie", autopct="%1.1f%%", figsize=(5,6), title="Expenses by Category")
    plt.ylabel("")
    plt.savefig("static/media/expense_per_category.jpg")


def plot_monthly_trends(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_summary = df.groupby("Month")["Amount"].sum()
    plt.figure()
    monthly_summary.plot(kind="bar", figsize=(5,6), title="Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Expenss")
    plt.xticks(rotation=45)
    plt.savefig("static/media/expenses_monthly_trend.jpg")


@app.route("/", methods=["GET", "POST"])
def home():
    df = None
    categories = []
    with open(CATEGORY_FILE, 'r') as file:
        categories = file.readlines()
        
    if request.method == "POST":
        date_expense = request.form.get("date_expense")
        category = request.form.get("category")
        amount = request.form.get("amount")
        description = request.form.get("description")
        
        log_expense(
            date=date_expense,
            category=category,
            amount=amount,
            description=description
        )
        
    
        
    df = load_expenses()
    data = df.to_dict(orient="records")
    columns = df.columns
    plot_expenses_by_category(df)
    plot_monthly_trends(df)
    return render_template(
        "index.html",
        categories=categories,
        columns=columns,
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)