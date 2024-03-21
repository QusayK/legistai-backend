class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://legistai-server:Sql%40123123@sql-test-legistai.database.windows.net:1433/legistai.db?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'kjrdgfdgaslkaspodkasodksadgeugurgdf'
    WTF_CSRF_ENABLED = False