import java.util.Scanner;

public class StringUtil {
	
	public static void reverse(String revs,int indx){
		if ( revs.length() - 1 > indx){
			reverse(revs,indx+1);			
		}
		System.out.print(revs.charAt(indx));		
	}
	public static void main(String ...args){
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter String");
		String str = scan.nextLine();
		if (str.length() > 0 )
			StringUtil.reverse(str, 0);
		scan.close();
	}

}
