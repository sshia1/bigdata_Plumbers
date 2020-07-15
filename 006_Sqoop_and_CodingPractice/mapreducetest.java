package mapreducetest;
import java.util.Map;
import java.util.Scanner;


public class mapreducetest {
	static void file_read() {
		System.out.println("file_read()");
	}
	
	static void TextInputFormat() {
		System.out.println("TextInputFormat()");
	}
	
	static void mapper() {
		System.out.println("mapper()");
	}
	
	static void partitioner() {
		System.out.println("partitioner()");
	}
	
	static void shuffle_and_sort() {
		System.out.println("shuffle_and_sort()");
	}
	
	static void reducer() {
		System.out.println("reducer()");
	}
		
	public static void main(String[] args) {
		System.out.println("entered main()");
		file_read();
		TextInputFormat();
		mapper();
		partitioner();
		shuffle_and_sort();
		reducer();
	}
		
}
