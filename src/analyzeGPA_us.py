class AnalyzeGPA_US:
    def __init__(self, cource_list):
        self.cource_list = cource_list

    def get_gpa(self):
        sum_gp_by_credits = 0.0
        sum_credits = 0.0

        for cource_dict in self.cource_list:
            gp_us = self.grade_points_to_gp(cource_dict["grade_points"])
            print("{}:\t{}".format(cource_dict["course_title"], gp_us))

            sum_gp_by_credits += gp_us * cource_dict["credits"]
            sum_credits += cource_dict["credits"]

        gpa_us = sum_gp_by_credits / sum_credits
        return gpa_us

    def grade_points_to_gp(self, grade_points):
        if grade_points > 92.4:  # A
            return 4
        elif grade_points > 89.9:  # A-
            return 3.7
        elif grade_points > 87.4:  # B+
            return 3.33
        elif grade_points > 82.4:  # B
            return 3
        elif grade_points > 79.9:  # B-
            return 2.7
        elif grade_points > 77.4:  # C+
            return 2.3
        elif grade_points > 72.4:  # C
            return 2
        elif grade_points > 69.9:  # C-
            return 1.7
        elif grade_points > 67.4:  # D+
            return 1.3
        elif grade_points > 62.4:  # D
            return 1
        elif grade_points > 59.0:  # D-
            return 0.7
        else:  # F
            return 0


if __name__ == "__main__":
    from main import main
    agpa_us = AnalyzeGPA_US(main())
    print(agpa_us.get_gpa())
