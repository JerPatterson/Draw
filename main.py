import draw

def main():
    encryption_key = "tetk" #TODO the key should not be choose by the user and different at every draw
    participant_names = ["Eliott", "Jerem", "Jeremie", "Jeremi", "Raphael", "Charles", "Guy", "Vincent", "Simon"]

    result = draw.make_draw(participant_names)
    draw.print_draw(result)

    encrypted_result = draw.encrypt_draw(result, encryption_key)
    draw.print_draw(encrypted_result)

if __name__ == "__main__":
    main()