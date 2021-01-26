class Merge:
    def __init__(self, letter, names):
        self.letter = letter
        self.names = names
        self.output_path = "./Output/ReadyToSend/"
    
    def merge(self):
        with open(self.letter, "r") as file:
            self.letter = file.readlines()

        with open(self.names, "r") as file:
            self.names = file.readlines()

        for name in self.names:
            record_count = len(self.names)
            new_letter = self.letter.copy()
            new_name = name.strip("\n")
            new_filename = f"{self.output_path}Letter_for_{new_name}.txt"
            new_line = new_letter[0].replace("[name]", new_name)
            new_letter[0] = new_line
            
            with open(new_filename, "w") as file:
                file.writelines(new_letter)
            
            return record_count

        
        