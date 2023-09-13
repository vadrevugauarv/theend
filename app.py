import streamlit as st
import random

def assign_students_and_experiments(exps, stu, spt, low, up):
    # Assignment of student roll numbers
    a = list(range(low, min(low + stu, up + 1)))

    # Random assignment of student numbers
    random.shuffle(a)

    # Assignment of experiments to array
    e = list(range(1, exps + 1))

    return a, e

def main():
    st.title("Student and Experiment Assignment")

    exps = st.number_input("Enter the number of experiments", min_value=1, step=1)
    stu = st.number_input("Enter the number of students", min_value=1, step=1)
    spt = st.number_input("Enter the number of students per bench", min_value=1, step=1)
    low = st.number_input("Enter the starting student number", min_value=1, step=1)
    up = st.number_input("Enter the ending student number", min_value=1, step=1)

    if st.button("Result"):
        a, e = assign_students_and_experiments(exps, stu, spt, low, up)

        k = 1  # No. of tables
        m = 0  # Experiment index

        # Printing all the details: student nos, exp nos, tables, etc.
        for i in range(stu):
            if i % spt == 0:
                st.write("\n_____________________________________________________")
                st.write(f"Table {k} :-")
                k += 1

            if m > len(e) - 1:
                m = 0

            st.write(f"{a[i]}-e:{e[m]}", end="  ")
            m += 1

if __name__ == "__main__":
    main()
