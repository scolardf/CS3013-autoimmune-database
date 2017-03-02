
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class CSVparser {
	public static void main(String[] args) throws IOException {
		PrintWriter writer = new PrintWriter("/Users/caolan/Desktop/Programming Project/SQLscript.txt", "UTF-8");
		String csvFile = "/Users/caolan/Desktop/Programming Project/EQ5Dcsv.csv";
		BufferedReader br = null;
		BufferedReader br2 = null;
		String line = "";
		String line2 = "";
		br = new BufferedReader(new FileReader(csvFile));
		br2 = new BufferedReader(new FileReader(csvFile));
		br.readLine(); //first line is not needed
		br2.readLine();//first line is not needed
		while((line = br.readLine())!=null){
			String[] data = line.split(",");
			writer.println("INSERT INTO Patients VALUES (");
			writer.println("'"+data[13]+"','"+data[9]+"','"+data[10]+"','"+data[11]+"','"+data[1]+"','"+""+"','"+data[14]+"','"+""+"','"+"EQ5D Export"+"','"+"Patient"+"');");
		}
		while((line2 = br2.readLine())!=null){
			String[] data2 = line2.split(",");
			System.out.println(data2[41]);
			writer.println("INSERT INTO Visit VALUES (");
			writer.println("'"+data2[29]+"','"+data2[30]+"','"+data2[32]+"','"+data2[31]+"','"+data2[33]+
					"','"+data2[0]+"','"+data2[29]+data2[30]+data2[32]+data2[31]+data2[33]+
					"','"+data2[41]+"','"+data2[1]+"','"+"undisclosed"+"','"+"undisclosed"+
					"','"+data2[22]+"','"+data2[23]+"','"+data2[25]+"','"+data2[26]+
					"','"+data2[15]+"','"+data2[18]+"','"+data2[17]+"','"+data2[19]+"','"+data2[20]+"','"+"algorithm"+"');");
		}
		br.close();
		br2.close();
		String CSVFile2 = "/Users/caolan/Desktop/Programming Project/Copy of Ireland & UK EQ5D Masterfile.csv";
		BufferedReader br3 = null;
		BufferedReader br4 = null;
		br3 = new BufferedReader(new FileReader(csvFile));
		br4 = new BufferedReader(new FileReader(csvFile));
		br3.readLine();//lines not needed
		br4.readLine();//lines not needed
		while((line = br3.readLine())!=null){
			String data3[] = line.split(",");
			
		}
	}
}
