class Member:
    def __init__(self, name, address, email, student_number, major):
        self.name = name
        self.address = address
        self.email = email
        self.student_number = student_number
        self.major = major
        self.info_list = [self.name, self.address, self.email, self.student_number, self.major]
        
    def print_info(self):
        print(self.info_list)


student_list = Member("Jiyoung Song", "Seoul", "-", "-", "Bioinformatics")
student_list.print_info()