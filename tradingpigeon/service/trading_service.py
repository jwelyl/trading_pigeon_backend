from pandas_datareader import data


class TradingService:
    def getTradingInfo(self, code: str, start_date: str, end_date: str):
        """
        임시 : yahoo financial 정보 불러오기
        Temp : Getting information of yahoo financial
        """
        # TODO : code 불러오기, 코스피는 .ks, 코스닥은 .kq
        # TODO 2 : 일단 static한 excel 불러오기
        # TODO 3 : DB 연결 이후에는 코드명 전부 저장
        # TODO 4 : 궁극적으로는 웹에서 excel 업로드하여 코드명 업데이트 가능하도록
        google_data = data.DataReader(code, "yahoo", start_date, end_date)
        google_data.head(9)
