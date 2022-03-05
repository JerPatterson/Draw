import draw_logic

def main():
    participant_names = ["Eliott", "Raphael", "Charles", "Guy", "Vincent", "Simon"]

    result = draw_logic.make_draw(participant_names)
    draw_logic.print_draw(result)

if __name__ == "__main__":
    main()