import sqlite3



def create_database():


    conn = sqlite3.connect(
        "resumes.db"
    )


    cursor = conn.cursor()



    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS candidates
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            skills TEXT,

            score REAL,

            missing_skills TEXT

        )
        """
    )



    conn.commit()

    conn.close()




def save_candidate(
        name,
        skills,
        score,
        missing
):


    conn = sqlite3.connect(
        "resumes.db"
    )


    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO candidates
        (
            name,
            skills,
            score,
            missing_skills
        )

        VALUES(?,?,?,?)
        """,

        (
            name,
            str(skills),
            score,
            str(missing)
        )
    )


    conn.commit()

    conn.close()