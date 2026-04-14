from models.student import student


class result(student):

    @property
    def total(self):
         return(self.english_mark + self.hindi_mark + self.sst_mark + self.science_mark + self.maths_mark)

    @property
    def percentage(self):
         return(self.total/500*100)


