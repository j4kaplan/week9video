import openpyxl
import openpyxl.utils

def get_good_linux_games(worksheet):
    game_count = 0
    for row in worksheet.rows:
        linux_column_number = openpyxl.utils.cell.column_index_from_string('AB')-1
        runs_on_linux = row[linux_column_number].value
        if runs_on_linux != "True":
            continue
        game_count +=1
        metircritic_cal_num= openpyxl.utils.cell.column_index_from_string('J')-1
    print(f"there are {game_count} games that run on linux")

def main():
    games_xcel_file = openpyxl.load_workbook("games-features.xlsx")
    game_sheet = games_xcel_file.active
    get_good_linux_games(game_sheet)

main()