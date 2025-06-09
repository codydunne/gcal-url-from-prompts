# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

# Run with:
# uv run --script .\gcal-url-from-prompts.py


import urllib.parse
from datetime import datetime


def main() -> None:

    print("\nCreating a link that generates a GCal event.\n")

    text = startDate = startDate = endDate = startTime = endTime = details = (
        location
    ) = ""

    def genStr(final=False):

        # https://calendar.google.com/calendar/render?action=TEMPLATE&text=
        # &dates=
        # &details=
        # &location=

        def safe_or_not(var):
            return urllib.parse.quote_plus(var) if final else var

        mainStr = (
            f"{'&' if final else '\n'}dates={safe_or_not(startDate)}"
            f"{'T' if final else ' T '}{safe_or_not(startTime)}"
            f"{'/' if final else ' / '}"
            f"{safe_or_not(endDate)}"
            f"{'T' if final else ' T '}"
            f"{safe_or_not(endTime)}"
            f"{'&' if final else '\n'}text={safe_or_not(text)}"
            f"{'&' if final else '\n'}details={safe_or_not(details)}"
            f"{'&' if final else '\n'}location={safe_or_not(location)}"
            f"{'' if final else '\n'}"
        )
        if not final:
            print(mainStr)
        return mainStr

    startDate = input(
        "Enter the start date in the format YYYYMMDD. If this year, just enter MMDD: "
    )

    if len(startDate) == 4:
        startDate = str(datetime.now().year) + startDate

    genStr()

    startTime = input(
        "Enter the start time in the format HHMM (24-hr) (can just enter HH): "
    )

    if len(startTime) == 2:
        startTime += "00"

    genStr()

    endDate = input(
        "Enter the end date in the format YYYYMMDD. If this year, just enter MMDD. If the same as before, don't enter anything: "
    )

    if len(endDate) == 4:
        endDate = str(datetime.now().year) + endDate

    elif endDate == "":
        endDate = startDate

    genStr()

    endTime = input(
        "Enter the end time in the format HHMM (24-hr) (can just enter HH): "
    )

    if len(endTime) == 2:
        endTime += "00"

    genStr()

    text = input("Enter the name of the event: ")

    genStr()

    details = input("Enter the event details: ")

    genStr()

    location = input("Enter the event location: ")

    genStr()

    print("Final result:\n")

    startTime += "00"
    endTime += "00"

    url = f"https://calendar.google.com/calendar/render?action=TEMPLATE{genStr(final=True)}"

    print(url, "\n")


if __name__ == "__main__":
    main()
