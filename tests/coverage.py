#pylint: disable=invalid-name
#using this name is not huriting anything.
#pylint: disable=no-member
#using this name is not huriting anything.

"""
Use this plugin to activate coverage report.

To install this plugin, you need to activate ``coverage-plugin``
with extra requirements :

::

    $ pip install nose2[coverage-plugin]


Next, you can enable coverage reporting with :

::

    $ nose2 --with-coverage

Or with this lines in ``unittest.cfg`` :

::

    [coverage]
    always-on = True


"""
from nose2.events import Plugin


class Coverage(Plugin):
    """
    this is coverage class
    """
    configSection = 'coverage'
    commandLineSwitch = ('C', 'with-coverage', 'Turn on coverage reporting')

    def __init__(self):
        """Get our config and add our command line arguments."""
        self.conSource = self.config.as_list('coverage', [])
        self.conReport = self.config.as_list('coverage-report', [])
        self.conConfig = self.config.as_str('coverage-config', '').strip()
        self.covSource = self.config.as_str('coverage-source', '').strip()

        group = self.session.pluginargs
        group.add_argument(
            '--coverage', action='append', default=[], metavar='PATH',
            dest='coverage_source',
            help='Measure coverage for filesystem path (multi-allowed)'
        )
        group.add_argument(
            '--coverage-report', action='append', default=[], metavar='TYPE',
            choices=['term', 'term-missing', 'annotate', 'html', 'xml'],
            dest='coverage_report',
            help='Generate selected reports, available types:'
                 ' term, term-missing, annotate, html, xml (multi-allowed)'
        )
        group.add_argument(
            '--coverage-config', action='store', default='', metavar='FILE',
            dest='coverage_config',
            help='Config file for coverage, default: .coveragerc'
        )

    def handleArgs(self, event):
        """Get our options in order command line, config file, hard coded."""

    def afterSummaryReport(self, event):
        """Only called if active so stop coverage and produce reports."""

        