// required fasttext results; 
import java.io.*;
import java.util.StringTokenizer;
import java.util.Hashtable;
import java.util.zip.GZIPInputStream;


public class FastTextPredictionFeaturesOrdered {

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

		while (str != null) {
			str = str.trim();

			String a = str.substring(0, str.indexOf("\t")); 
			String fake = new String(); String trust = new String(); 
			//String satire = new String(); 

			String delim = " ";
			String[] entry;
			entry = a.split(delim);

			for (int i=0; i<entry.length; i++) {
				String tok = entry[i];
				if (tok.equals("trusted")) trust = entry[i+1];
				else if (tok.equals("fakeNews")) fake = entry[i+1];
				//else if (tok.equals("satire")) satire = entry[i+1];
				else {}

			}
			//System.out.println("trusted " + trust + " " + "fakeNews " + fake + " " + "satire " + satire + "\t en");
			System.out.println("trusted " + trust + " " + "fakeNews " + fake + " " + "\t yt");

			str = d.readLine();
		}
		d.close();
	}
}
