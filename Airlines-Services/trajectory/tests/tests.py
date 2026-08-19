
from trajectory.Environment.WindTemperature.WindTemperatureFetch import fetchWindTemperature


if __name__ == '__main__':

    USregion = "All"
    ForecastHour = "12-Hour"
    Level = "low"
    
    weatherDataList = fetchWindTemperature(USregion , ForecastHour, Level)
    lineNumber = 1
    for weatherDataLine in weatherDataList:
        print ( "line number = {0} - weatherDataLine = {1}".format( str(lineNumber) , weatherDataLine ) )
        lineNumber = lineNumber + 1


        