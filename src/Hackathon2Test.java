import java.io.*;
import java.util.StringTokenizer;
import java.util.Hashtable;
import java.util.zip.GZIPInputStream;


public class Hackathon2Test  { // test.tsv with 3 columns; 

	public static void main (String[] args) throws IOException {

		String fileName = args[0];
		//	BufferedReader d = new BufferedReader(new InputStreamReader(new FileInputStream(new File (fileName))));
		//                OutputStreamWriter out = new OutputStreamWriter (new FileOutputStream(fileName+".1"), "UTF-8");
		BufferedReader d;
		if (fileName.endsWith(".gz")) {
			d = new BufferedReader(new InputStreamReader(new GZIPInputStream(new FileInputStream(new File(fileName)))));
		}
		else {
			d = new BufferedReader(new InputStreamReader(new FileInputStream(new File(fileName))));
		}
		String str = new String();
		str = d.readLine();

		String line = new String(); 

		while (str != null) {
			//str = str.trim();
			str = str.replaceAll("\"\"", "\"");
			if (str.contains("\t")) {
				if (line.length()>0) {
					System.out.println(line); line = new String(); 
				}
				line = str; 
			}
			else {
				line += " " + str; 
			}
			str = d.readLine();
		}
		if (line.length()>0) {
			System.out.println(line); line = new String();
		}

		d.close();
	}
}

