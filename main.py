from pathlib import Path
def load_text(path):
    return Path(path).read_text(encoding="utf-8")

def main():
    resume=load_text("data/resume/resume1.txt")
    jd=load_text("data/job_description/jd1.txt")

    print("==AI SYSTEM==")
    print("==Your Resume==")
    print(resume)

    print("==Job description==")
    print(jd)

if __name__== "__main__":
    main()

