import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class AppDataParser {
	public static void main(String[] args) throws IOException {
		PrintWriter writer = new PrintWriter("/Users/caolan/Desktop/Programming Project/SQLscriptAppData.txt", "UTF-8");
		String csvFile = "/Users/caolan/Desktop/Programming Project/dummy eq5d data for students values.csv";
		BufferedReader br = null;
		String line = "";
		br = new BufferedReader(new FileReader(csvFile));
		br.readLine(); // first line is not needed
		int counter = 0;
		while((line = br.readLine())!=null){
			String[] data = line.split(",");
			if(data.length==4){
				String[] newData = new String[10];
				for(int i = 0;i<data.length-1;i++){
					newData[i] = data[i];
				}
				for(int i2 = 4;i2<=9;i2++){
					newData[i2] = "NULL";
				}
				data = newData;
			}
			writer.println("INSERT INTO appdata VALUES ('");
			writer.println(data[1]+"','"+data[4]+"','"+data[5]+"','"+data[6]+"','"+data[7]+
					"','"+data[8]+"','"+data[9]+"','"+data[0]+"');");
			System.out.println(counter);
		}
		writer.flush();
		writer.close();
	}
}
