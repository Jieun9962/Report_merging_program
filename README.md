# PDF Report Merging Automation🖥️
PDF 보고서 병합 및 오류 요약 자동화 with 파이썬

Automating PDF report consolidation and error summary generation with Python

## 프로젝트 개요 - Project Overview

개인이 진행한 프로젝트 입니다.
Gemini, ChatGPT를 활용하였습니다.
PDF 보고서 병합 및 오류 집계 작업을 자동화하기 위해 진행한 Python 프로젝트 입니다.
간지 별로 페이지를 분류하고 템플릿 항목의 순서에 맞추어 하나의 PDF로 병합 후 체크 항목별 오류 건수를 집계하여 Excel 파일로 생성합니다.

이 프로젝트는 실제 업무에서 수행했던 보고서 처리 자동화 경험을 바탕으로 제작한 포트폴리오용 데모 프로젝트 입니다.

✂️대외비로 인하여 중요 정보 누출 가능성이 조금이라도 있는 코드 부분을 포함하여, 모든 입력 파일과 템플릿은 실무에서 사용하던 것이 아닌 임의로 제작한 파일로 구성되어 있습니다.

Personal Project
Used Gemini, ChatGPT
This Python project automates the process of merging PDF reports and counting errors.
It sorts pages by section, merges them into a single PDF in the order specified by the template, and exports the error count for each checklist item to an Excel file.

This is a portfolio demo based on my experience automating report-processing tasks in a real work environment.
To protect confidential information, I created the code and all input files and templates specifically for this demo rather than using materials from my previous work. This also applies to code that might otherwise reveal internal information.

## 주요기능 - Key Features
- PDF 페이지 분류 및 템플릿 기반 병합 : PDF 보고서의 페이지를 확인하고 체크 항목에 따라 분류하며 지정된 템플릿 구조와 체크 항목 순서에 맞춰 페이지를 병합합니다.
- 오류 건수 집계 : 체크 항목별 오류 건수를 집계합니다.
- Excel 요약 생성 : 집계 결과를 Excel 파일로 출력합니다.
- 폴더 선택 인터페이스 : 사용자가 파일이 포함된 폴더를 직접 선택할 수 있습니다.

- PDF Page Sorting and Template-Based Merging: Identifies pages in PDF reports, sorts them by checklist item, and merges them in the order specified by the template.
- Error Count Summary: Counts errors for each checklist item.
- Excel Summary Generation: Exports the results to an Excel file.
- Folder Selection: Allows users to select the folder containing the input files.

 ## 프로젝트 구조 - Project Structure
report_merging_demo/
├── src/
│   └── demo_merger.py
├── input/
│   ├── demo_template.pdf
│   ├── sample_report_alpha.pdf
│   └── sample_report_beta.pdf
├── output/
│   ├── merged_demo_report.pdf
│   └── demo_error_summary.xlsx
├── requirements.txt
├── .gitignore
└── README.md

## 실행법 - How to Run
1. 코드 실행 전 확인 사항 : Python 설치, 프로젝트 파일 다운로드 또는 GitHub 저장소 복제 (Output 파일은 제외하고 다운해야 코드 동작 확인 가능)
2. 필요한 라이브러리 설치 : python -m pip install -r requirements.txt
3. 프로그램 실행 : python src/demo_merger.py

프로그램이 실행되면 입력 PDF 파일이 포함된 폴더를 선택합니다. 입력 파일 내에는 템플릿 파일(demo_template.pdf)이 병합할 리포트와 같은 장소에 저장되어 있어야 하며 템플릿 이름을 변경해서는 안됩니다.
처리가 완료되면 결과 파일이 output/ 디렉터리와 같이 생성 혹은 내에 생성 됩니다.

참고: 실행 환경에 따라 Python 인터프리터와 라이브러리 설치 환경이 일치하는지 확인해야 합니다.

1. Before Running : Install Python and download the project files or clone the GitHub repository. (Exclude the output/ directory when downloading the project if you want to test the program from scratch)
2. Install Dependencies : python -m pip install -r requirements.txt
3. Run Program : python src/demo_merger.py

When the program starts, select the folder containing the input PDF files.
The template file, demo_template.pdf, must be stored in the same folder as the reports to be merged. Do not rename the template file, as the program expects this exact filename.
Once processing is complete, the generated files will be saved in the output/ directory.

Note: Make sure that the Python interpreter used to run the program is the same one where the required libraries are installed.

## 프로젝트 의의 - Project Purpose
이 프로젝트는 보고서 처리 작업을 자동화 함으로써 반복되는 수작업을 최소화하고 결과물 생성 과정을 일관된 절차로 구성할 수 있도록 하는데 초점을 맞추었습니다.
이를 통하여 단순 반복 작업을 줄임으로써 고객사가 요청한 보고서를 전달하는데 소요되는 시간을 줄이는데 기여할 수 있었습니다.

This project focuses on reducing repetitive manual work in report processing and making report generation more consistent.
Automating these tasks helped reduce the time needed to prepare and deliver reports requested by clients.

## 데이터 및 보안 - Data and Confidentiality
- 모든 PDF 및 템플릿은 포트폴리오 시연을 위해 제작한 가상 데이터 입니다.
- 실제 고객사 정보, 업무 문서, 내부 체크리스트 및 기밀 자료는 포함하지 않았습니다.

- All PDF reports and templates are fictional files created specifically for this portfolio demo.
- No actual client information, work documents, internal checklists, or confidential materials are included.
