# function to identify patent or journals
def showFilePatentOrJournal:
try:
            with open(self.selectedTrainingFilePath, 'r+') as f:
                fileHeader = f.readline().strip()
        except:
            return

        if 'identification number\ttitle\tabstract\tclaims\tapplication number\tapplication date\tcurrent assignee\tupc' in fileHeader.lower():
            # it is patent data
            self.textVariableTrainingDataFileName.set(os.path.basename(self.selectedTrainingFilePath) + ' (Patents)')
            self.patentOrJournalTrainingData = 'Patent'

        elif 'meta data\ttitle\tabstract\tauthor\taffiliation\tpublished year' in fileHeader.lower():
            # it is journal data
            self.textVariableTrainingDataFileName.set(os.path.basename(self.selectedTrainingFilePath) + ' (Journals)')
            self.patentOrJournalTrainingData = 'Journal'

        elif 'nasca' in fileHeader.lower():
            tkMessageBox.showerror("NASCA File Error", "The input file appears to be encrypted using NASCA. Please remove NASCA encryption from the file and try again.")

