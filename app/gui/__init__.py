def __init__(self, parent):

    super().__init__(parent)

    self.statistics = StatisticsEngine()

    self.chart_generator = ChartGenerator()

    self.product_repo = ProductRepository()

    self.session_repo = SessionRepository()

    self.csv_exporter = CSVExporter()

    self.excel_exporter = ExcelExporter()

    self.json_exporter = JSONExporter()

    self.build_ui()

    self.load_stats()

    self.load_statistics()