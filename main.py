from progress.bar import Bar

def main():
    try:
        open("original.txt","r")
    except:
        open("original.txt","w")
    try:
        open("shortened.txt","r")
    except:
        open("shortened.txt","w")
        
    cleaned_text = clean()
    write(cleaned_text)
    check()
                
def clean():
    with open("original.txt","r") as original:
        original_text = original.readlines()
        if len(original_text) == 0:
            print("Please write to file")
            quit()
        else:
            cleaned_text=[]
            for line in original_text:
                if line not in cleaned_text or line == "\n":
                    cleaned_text.append(line)
            print(f"{len(original_text)-len(cleaned_text)} lines have been removed = {round(1-len(cleaned_text)/len(original_text),3)}% of file")
            return cleaned_text
            
    
    
def write(cleaned_text):
    writing_cleaned_text_bar = Bar('Importing cleaned text', max=len(cleaned_text))
    with open("shortened.txt","w") as f:
        pass
    with open("shortened.txt","a") as shortened:
        for line in cleaned_text:
            shortened.write(line)
            writing_cleaned_text_bar.next()
        writing_cleaned_text_bar.finish()
        print("Cleaning complete")
        
        
def check():
    long = open("original.txt","r").readlines()
    short = open("shortened.txt","r").readlines()
    missing_lines = []
    for line in long:
        if line not in short:
            print("Line missing")
            missing_lines.append(line)
    print(f"{len(missing_lines)} lines missing")
    print("Missing lines:")
    for line in missing_lines:
        print(line)
            
    

if __name__ == "__main__":
    main()