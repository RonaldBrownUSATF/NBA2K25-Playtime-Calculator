import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_game_time(rec_games):
    # Convert rec games to total hours
    total_rec_hours = rec_games * 0.5  # Each rec game is 30 minutes, or 0.5 hours

    # Calculate the total hours from September 6, 2024, 12:00 AM CST to now
    start_date = datetime(2024, 9, 6, 0, 0)
    current_date = datetime.now()
    total_hours_elapsed = (current_date - start_date).total_seconds() / 3600

    # Calculate the number of days elapsed
    days_elapsed = (current_date - start_date).days

    # Full-time work hours since release
    full_time_hours = days_elapsed * (40 / 7)

    # Calculate the percentage of total time spent playing rec games
    percentage_of_total_time = (total_rec_hours / total_hours_elapsed) * 100

    # Calculate the percentage of waking hours (16 hours per day)
    waking_hours = (current_date - start_date).days * 16
    percentage_of_waking_hours = (total_rec_hours / waking_hours) * 100 if waking_hours > 0 else 0

    # Calculate the percentage of free time (6 hours per day)
    free_hours = (current_date - start_date).days * 6
    percentage_of_free_time = (total_rec_hours / free_hours) * 100 if free_hours > 0 else 0

    # Convert total_rec_hours to days and fractional hours
    total_minutes = total_rec_hours * 60
    days = int(total_minutes // 1440)
    hours = (total_minutes % 1440) / 60  # Fractional hours

    return {
        "total_rec_hours": total_rec_hours,
        "percentage_of_total_time": percentage_of_total_time,
        "percentage_of_waking_hours": percentage_of_waking_hours,
        "percentage_of_free_time": percentage_of_free_time,
        "time_breakdown": f"{days} days and {hours:.2f} hours",
        "full_time_hours": full_time_hours  # Correctly included here
    }

def show_second_page():
    first_page.pack_forget()
    second_page.pack(fill="both", expand=True)

def calculate_and_display():
    try:
        rec_games = int(entry_rec_games.get())
        global game_time_result
        game_time_result = calculate_game_time(rec_games)

        output = (
            f"You have spent a total of {game_time_result['total_rec_hours']:.2f} hours playing rec. "
            f"That's {game_time_result['time_breakdown']}!\n\n"
            f"That means you have spent {game_time_result['percentage_of_total_time']:.2f}% of your time alive playing Rec on 2K25 since its release.\n"
            f"Which would be {game_time_result['percentage_of_waking_hours']:.2f}% of your hours awake.\n"
            f"Or just about {game_time_result['percentage_of_free_time']:.2f}% of your free time.\n"
            f"For reference, a full-time employee would have worked approximately {game_time_result['full_time_hours']:.2f} hours since 2K25's release."
        )

        messagebox.showinfo("Results", output)

        calculate_averages = messagebox.askyesno("Averages", "Would you like to calculate your averages?")
        if calculate_averages:
            show_second_page()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of rec games.")

def calculate_averages():
    try:
        rec_games = int(entry_rec_games.get())
        points = float(entry_points.get())
        rebounds = float(entry_rebounds.get())
        assists = float(entry_assists.get())
        steals = float(entry_steals.get())
        blocks = float(entry_blocks.get())
        turnovers = float(entry_turnovers.get())
        fouls = float(entry_fouls.get())
        fgp = float(entry_fgp.get())
        tpp = float(entry_tpp.get())
        ftp = float(entry_ftp.get())
        win_percentage = float(entry_win_percentage.get())

        # Calculate per game stats
        ppg = points / rec_games
        rpg = rebounds / rec_games
        apg = assists / rec_games
        spg = steals / rec_games
        bpg = blocks / rec_games

        # Calculate AST/TO ratio and S/F ratio
        ast_to_ratio = assists / turnovers if turnovers > 0 else 0
        stocks_to_foul_ratio = (steals + blocks) / fouls if fouls > 0 else 0

        averages_output = (
            f"You average {ppg:.1f}ppg/{rpg:.1f}rpg/{apg:.1f}apg/{spg:.1f}spg/{bpg:.1f}bpg. "
            f"Your Assist to Turnover ratio is {ast_to_ratio:.2f} and your Stocks to Foul ratio is {stocks_to_foul_ratio:.2f}. "
            f"You're doing all of this on {fgp:.1f}/{tpp:.1f}/{ftp:.1f} shooting splits while winning {win_percentage:.1f}% of your games."
        )

        messagebox.showinfo("Averages", averages_output)

        show_summary = messagebox.askyesno("Summary", "Would you like a summary?")
        if show_summary:
            summary_output = (
                f"You have spent {game_time_result['total_rec_hours']:.2f} hours playing Rec. "
                f"That's {game_time_result['time_breakdown']}. "
                f"That means you have spent {game_time_result['percentage_of_total_time']:.2f}% of your time alive playing Rec on 2K25 since its release. "
                f"Which would be {game_time_result['percentage_of_waking_hours']:.2f}% of your hours awake, or just about {game_time_result['percentage_of_free_time']:.2f}% of your free time. "
                f"For reference, a full-time employee would have worked approximately {game_time_result['full_time_hours']:.2f} hours since 2K25's release. "
                f"You've spent all of that time playing Rec for averages of {ppg:.1f}ppg/{rpg:.1f}rpg/{apg:.1f}apg/{spg:.1f}spg/{bpg:.1f}bpg. "
                f"Your Assist to Turnover ratio is {ast_to_ratio:.2f} and your Stocks to Foul ratio is {stocks_to_foul_ratio:.2f}. "
                f"You're doing all of this on {fgp:.1f}/{tpp:.1f}/{ftp:.1f} shooting splits while winning {win_percentage:.1f}% of your games."
            )
            messagebox.showinfo("Summary", summary_output)
        else:
            messagebox.showinfo("Summary", "Yes you do.")
            messagebox.showinfo("Summary", summary_output)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric inputs.")

def reset():
    entry_rec_games.delete(0, tk.END)
    entry_points.delete(0, tk.END)
    entry_rebounds.delete(0, tk.END)
    entry_assists.delete(0, tk.END)
    entry_steals.delete(0, tk.END)
    entry_blocks.delete(0, tk.END)
    entry_turnovers.delete(0, tk.END)
    entry_fouls.delete(0, tk.END)
    entry_fgp.delete(0, tk.END)
    entry_tpp.delete(0, tk.END)
    entry_ftp.delete(0, tk.END)

def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        messagebox.showinfo("Thank you for your time", "Remember to stretch daily!")
        root.destroy()

# Create the main application window
root = tk.Tk()
root.title("How Much 2K25 Do You Play? (Rec Edition)")
root.geometry("1040x800")

# First page
first_page = tk.Frame(root)
first_page.pack(fill="both", expand=True)

label_rec_games = tk.Label(first_page, text="How many rec games have you played?")
label_rec_games.pack(pady=5)

entry_rec_games = tk.Entry(first_page)
entry_rec_games.pack(pady=5)

button_calculate = tk.Button(first_page, text="Calculate", command=calculate_and_display)
button_calculate.pack(pady=5)

# Second page
second_page = tk.Frame(root)

label_points = tk.Label(second_page, text="Total Points:")
label_points.pack(pady=5)
entry_points = tk.Entry(second_page)
entry_points.pack(pady=5)

label_rebounds = tk.Label(second_page, text="Total Rebounds:")
label_rebounds.pack(pady=5)
entry_rebounds = tk.Entry(second_page)
entry_rebounds.pack(pady=5)

label_assists = tk.Label(second_page, text="Total Assists:")
label_assists.pack(pady=5)
entry_assists = tk.Entry(second_page)
entry_assists.pack(pady=5)

label_steals = tk.Label(second_page, text="Total Steals:")
label_steals.pack(pady=5)
entry_steals = tk.Entry(second_page)
entry_steals.pack(pady=5)

label_blocks = tk.Label(second_page, text="Total Blocks:")
label_blocks.pack(pady=5)
entry_blocks = tk.Entry(second_page)
entry_blocks.pack(pady=5)

label_turnovers = tk.Label(second_page, text="Total Turnovers:")
label_turnovers.pack(pady=5)
entry_turnovers = tk.Entry(second_page)
entry_turnovers.pack(pady=5)

label_fouls = tk.Label(second_page, text="Total Fouls:")
label_fouls.pack(pady=5)
entry_fouls = tk.Entry(second_page)
entry_fouls.pack(pady=5)

label_fgp = tk.Label(second_page, text="Field Goal Percentage (FG%):")
label_fgp.pack(pady=5)
entry_fgp = tk.Entry(second_page)
entry_fgp.pack(pady=5)

label_tpp = tk.Label(second_page, text="Three Point Percentage (3pt%):")
label_tpp.pack(pady=5)
entry_tpp = tk.Entry(second_page)
entry_tpp.pack(pady=5)

label_ftp = tk.Label(second_page, text="Free Throw Percentage (FT%):")
label_ftp.pack(pady=5)
entry_ftp = tk.Entry(second_page)
entry_ftp.pack(pady=5)

label_win_percentage = tk.Label(second_page, text="Win Percentage:")
label_win_percentage.pack(pady=5)
entry_win_percentage = tk.Entry(second_page)
entry_win_percentage.pack(pady=5)

button_calculate_averages = tk.Button(second_page, text="Calculate Averages", command=calculate_averages)
button_calculate_averages.pack(pady=5)

button_back = tk.Button(second_page, text="Back", command=lambda: [second_page.pack_forget(), first_page.pack(fill="both", expand=True)])
button_back.pack(pady=5)

button_exit = tk.Button(second_page, text="Exit", command=exit_program)
button_exit.pack(pady=5)

# Run the application
root.mainloop()
