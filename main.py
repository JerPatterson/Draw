from unicodedata import decimal
import draw_logic

def main():
    encryption_key = "tetk" #TODO the key should not be choose by the user and different at every draw
    participant_names = ["Eliott", "Raphael", "Charles", "Guy", "Vincent", "Simon"]

    result = draw_logic.make_draw(participant_names)
    draw_logic.print_draw(result)

    encrypted_result = draw_logic.encrypt_draw(result, encryption_key)
    draw_logic.print_draw(encrypted_result)

if __name__ == "__main__":
    main()