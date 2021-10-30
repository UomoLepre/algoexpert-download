from downloaders.question_data.question_data_downloader import main as download_question_data
from downloaders.question_pdf.question_pdf_downloader import main as download_question_pdf
from downloaders.question_solution.question_solution_video_downloader import main as download_question_solution_videos

from config import RUN_download_question_data, RUN_download_question_pdf, RUN_download_question_solution_videos

def main():
    if RUN_download_question_data:
        download_question_data()
    if RUN_download_question_pdf:
        download_question_pdf()
    if RUN_download_question_solution_videos:
        download_question_solution_videos()

if __name__ == "__main__":
    main()