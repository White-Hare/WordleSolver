def main():    
    print("Language:")
    language = str(input())

    with open(language + "_words.txt", "r", encoding="utf-8") as file:
        words = file.read().replace("\"", "").replace("\n", "").split(",")
        


        while len(words) > 0:
            print("Placed Characters:")
            placed_characters = str(input()).lower()
            if placed_characters.isdigit():
                placed_characters = int(placed_characters) * "_"
                

            
            print("Unplaced Characters:")
            unplaced_characters = str(input()).lower()

            print("Excluded Characters:")
            excluded_characters = str(input()).lower()
            
            
            possible_results = []
            for word in words:
                possible = True

                for c in range(len(placed_characters)):    
                    if placed_characters[c] != word[c] and placed_characters[c] not in ["_", " ", "."]:
                        possible = False


                if not possible:
                    continue


                for c in unplaced_characters:
                    if c not in word:
                        possible = False
                        break       

                if not possible:
                    continue


                for c in excluded_characters:
                    if c in word:
                        possible = False
                        break       

                if not possible:
                    continue


                possible_results.append(word)



            print(possible_results)
            words = possible_results


if __name__ == "__main__":
    main()