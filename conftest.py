import pytest


# def pytest_terminal_summary(terminalreporter):
#     with open(f"test_report_{'TP'}.txt", "w") as f:
#         summary = (
#             f"Total: {len(terminalreporter.stats.get('passed', [])) + len(terminalreporter.stats.get('failed', []))}, "
#             f"Passed: {len(terminalreporter.stats.get('passed', []))}, "
#             f"Failed: {len(terminalreporter.stats.get('failed', []))}\n"
#         )
#         f.write(summary)
#         f.write("Failed cases:\n")
#         for result in terminalreporter.stats.get('failed', []):
#             f.write(f"{result.nodeid}\n")


def pytest_configure(config):
    config.results = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when in ("setup", "call"):
        outcome = 'PASSED' if report.passed else 'FAILED' if report.failed else 'SKIPPED'
        config = item.config
        config.results.append({
            'name': report.nodeid,
            'phase': report.when,
            'status': outcome
        })


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    summary_results = {}
    summary = {
        'PASSED': 0,
        'FAILED': 0
    }
    failed_case = []

    for result in config.results:
        summary_results[result['name']] = result['status']
    for item in summary_results:
        print(item, summary_results[item])
    for case in summary_results:
        if summary_results[case] == 'PASSED':
            summary['PASSED'] += 1
        elif summary_results[case] == 'FAILED':
            summary['FAILED'] += 1
            failed_case.append(case)

    with open(f"test_report_{'NTP'}.txt", "w") as f:
        f.write(f"Total: {summary['PASSED'] + summary['FAILED']}, Passed: {summary['PASSED']}, Failed: {summary['FAILED']}\n")
        f.write("Failed cases:\n")
        f.write("\n".join(failed_case))
        f.write("\n")
