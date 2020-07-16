package mapreducetest;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;

public class mapreducetest {
   //static String text_filename = "/home/field/Downloads/temp.txt";
   static String text_filename = "/home/field/Downloads/Shakespeare.txt";
	
   public static void main(String[] args) throws IOException {
      File           f1 = new File(text_filename); 
      String[]    words = null;
      int            wc = 0;   
      FileReader     fr = new FileReader(f1);  
      BufferedReader br = new BufferedReader(fr); 
      String s;
      Hashtable<String,Integer> word_count = new Hashtable<String,Integer>();
      
      while((s=br.readLine())!=null) {
         words = s.split(" ");  
         
         int i = 0;
         for(i = 0; i < words.length; i++) {
        	 System.out.println(words[i]);
        	 if (word_count == null || word_count.size() == 0) {
        		 word_count.put(words[i], 1);
        	 } 
        	 else {
        		 if (! word_count.contains(words[i])) {
        			 word_count.put(words[i], 1);
        		 }
        		 else {
        			 int count = word_count.get(words[i]);
        			 count += 1;
        			 word_count.put(words[i], count);
        		 }
        	 }
         }
      }
      fr.close();
      
      System.out.println(word_count);
   }
}
