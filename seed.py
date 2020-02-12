from model import (Program, Section, Activity, Answer, db, connect_to_db)

def example_data():
    """ Create some sample data. """

    #Programs
    first_program = Program(name="Leadership Development Program",
                            description="Leadership Development Program Description")

    second_program = Program(name="Cognitive Behavioral Therapy",
                            description="Cognitive Behavioral Therapy Description")

    third_program = Program(name="New Parenting",
                            description="New Parenting Description")

    fourth_program = Program(name="Mindful Communication",
                            description="Mindful Communication Description")

    
    #First program's sections
    section_1 = Section(program_id= 1, 
                        name= "Section 1 Program 1'",
                        description= "Section 1 Program 1 Description",
                        order_index= 1,
                        image_link= "",
                        is_last= False)

    section_2 = Section(program_id= 1, 
                        name= "Section 2 Program 1'",
                        description= "Section 2 Program 1 Description",
                        order_index= 2,
                        image_link= "",
                        is_last= False)

    section_3 = Section(program_id= 1, 
                        name= "Section 3 Program 1'",
                        description= "Section 3 Program 1 Description",
                        order_index= 3,
                        image_link= "",
                        is_last= False)

    section_4 = Section(program_id= 1, 
                        name= "Section 4 Program 1'",
                        description= "Section 4 Program 1 Description",
                        order_index= 4,
                        image_link= "",
                        is_last= False)

    section_5 = Section(program_id= 1, 
                        name= "Section 5 Program 1'",
                        description= "Section 5 Program 1 Description",
                        order_index= 5,
                        image_link= "",
                        is_last= False)

    section_6 = Section(program_id= 1, 
                        name= "Section 6 Program 1'",
                        description= "Section 6 Program 1 Description",
                        order_index= 6,
                        image_link= "",
                        is_last= False)

    section_7 = Section(program_id= 1, 
                        name= "Section 7 Program 1'",
                        description= "Section 7 Program 1 Description",
                        order_index= 7,
                        image_link= "",
                        is_last= False)

    section_8 = Section(program_id= 1, 
                        name= "Section 8 Program 1'",
                        description= "Section 8 Program 1 Description",
                        order_index= 8,
                        image_link= "",
                        is_last= False)

    section_9 = Section(program_id= 1, 
                        name= "Section 9 Program 1'",
                        description= "Section 9 Program 1 Description",
                        order_index= 9,
                        image_link= "",
                        is_last= False)

    section_10 = Section(program_id= 1, 
                        name= "Section 10 Program 1'",
                        description= "Section 10 Program 1 Description",
                        order_index= 10,
                        image_link= "",
                        is_last= False)

    activity_1 = Activity(section_id=1,
                        html_content="",
                        question="Question Activity 1")
                    
    activity_2 = Activity(section_id=2,
                        html_content="<html></html>",
                        question="")

    answer_1 = Answer(activity_id=1,
                    answer_text="Activity 1 Answer Text")


    db.session.add_all([first_program, second_program, third_program, fourth_program, section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8, section_9, section_10, activity_1, activity_2, answer_1])
    db.session.commit()

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
