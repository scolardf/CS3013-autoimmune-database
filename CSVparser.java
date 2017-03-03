
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
			String[] date = null;
			String newDate = null;
			if(data[1].isEmpty()==false){
			date = data[1].split("/");
			newDate = date[2]+"-"+date[1]+"-"+date[0];
			}
			if(newDate == null){
				newDate = "0000-00-00";
			}
			writer.println("INSERT INTO Patients VALUES (");
			writer.println("'"+data[13]+"','"+data[9]+"','"+data[10]+"','"+data[11]+"','"+newDate+"','"+""+"','"+data[14]+"',"+"NULL"+",'"+"EQ5D Export"+"','"+"Patient"+"');");
		}
		while((line2 = br2.readLine())!=null){
			String[] data2 = line2.split(",");
			String[] date = data2[0].split("/");
			String[] date2 = null;
			String newDate2 = null;
			if(data2[1].isEmpty()==false){
				date2 = data2[1].split("/");
				newDate2 = date2[2]+"-"+date2[1]+"-"+date2[0];
			}
			if(newDate2 == null){
				newDate2 = "0000-00-00";
			}
			String newDate = date[2]+"-"+date[1]+"-"+date[0];
			writer.println("INSERT INTO Visit VALUES (");
			writer.println("'"+data2[29]+"','"+data2[30]+"','"+data2[32]+"','"+data2[31]+"','"+data2[33]+
					"','"+newDate+"','"+data2[29]+data2[30]+data2[32]+data2[31]+data2[33]+
					"','"+data2[41]+"','"+newDate2+"','"+"undisclosed"+"','"+"undisclosed"+
					"','"+data2[22]+"','"+data2[23]+"','"+data2[25]+"','"+data2[26]+
					"','"+data2[15]+"','"+data2[18]+"','"+data2[17]+"','"+data2[19]+"','"+data2[20]+"','"+data2[13]+"',"+"NULL"+");");
		}
		br.close();
		br2.close();
		String CSVFile2 = "/Users/caolan/Desktop/Programming Project/Copy of Ireland & UK EQ5D Masterfile.csv";
		BufferedReader br3 = null;
		BufferedReader br4 = null;
		br3 = new BufferedReader(new FileReader(CSVFile2));
		br4 = new BufferedReader(new FileReader(CSVFile2));
		br3.readLine();					//lines not needed
		br4.readLine();					//lines not needed
		while((line = br3.readLine())!=null){
			String data3[] = line.split(",");
			String newDate = null;
			if(data3[21].isEmpty()==false){
				String[] date = data3[21].split("/");
				newDate = date[2]+"-"+date[1]+"-"+date[0];
			}
			if(newDate == null){
				newDate = "0000-00-00";
			}
			System.out.println(newDate);
			writer.println("INSERT INTO Patients VALUES (");
			writer.println("'"+data3[0]+"','"+data3[4]+"','"+data3[5]+"','"+
			data3[24]+"','"+newDate+"','"+data3[20]+"','"+data3[19]+"','"+data3[22]+
			"','"+"Ireland & UK EQ5D"+"','"+data3[23]+	"');");
		}
		while((line = br4.readLine())!=null){
			String data4[] = line.split(",");
			String newDate = null;
			if(data4[3].isEmpty()==false){
				String[] date = data4[3].split("/");
				newDate = date[2]+"-"+date[1]+"-"+date[0];
			}
			if(newDate == null){
				newDate = "0000-00-00";
			}
			int healthScore = 0;
			if(data4[18].isEmpty()==false){
				healthScore = Integer.parseInt(data4[18]);
			}
			if(Double.parseDouble(data4[17]) == 1.000){
				data4[17]="1.000";
			}	
			writer.println("INSERT INTO Visit VALUES (");
			writer.println("'"+data4[6]+"','"+data4[8]+"','"+data4[10]+"','"+data4[12]+"','"+data4[14]+"','"+
			newDate+"','"+data4[6]+data4[8]+data4[10]+data4[12]+data4[14]+"','"+healthScore+"',"+"NULL"+",'"+data4[25]+"','"+data4[34]+"','"+data4[33]+"','"+
			data4[35]+"','"+data4[36]+"','"+data4[26]+"','"+data4[27]+"','"+data4[28]+"','"+
			data4[29]+"','"+data4[30]+"','"+data4[31]+"','"+data4[0]+"','"+data4[17]+"');");
		}
		writer.flush();
		writer.close();
		br3.close();
		br4.close();
	}
}
