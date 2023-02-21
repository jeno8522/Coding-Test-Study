import java.util.Scanner;

class ListNode{
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

class List{
	ListNode header = null;
	ListNode trailer = null;
	
	void insertNode(int data) {
		ListNode newNode = new ListNode(data);
		
		if(this.header == null && this.trailer == null) {
			this.header = newNode;
			this.trailer = newNode;
		}
		else {
			this.trailer.next = newNode;
			this.trailer = this.trailer.next;
		}
	}
	
	int deleteNode(ListNode sub, ListNode deletion) {
		int num = deletion.val;
		sub.next = deletion.next;
		
		deletion.next = null;
		deletion = null;
		
		return num;
	}
}
public class Main_1158_S4_요세푸스문제_주창훈 {

	public static void main(String[] args) {
		List l = new List();
		ListNode tmp = l.header;
		int n, k;
		int res = 0;
		
		Scanner input = new Scanner(System.in);
		
		n = input.nextInt();
		k = input.nextInt();
		
		
		
		
		for(int i = 1; i <= n; i++) {
			l.insertNode(i);
		}
		l.trailer.next = l.header;
		
		
		
		tmp = l.header;
		ListNode sub = null;
		int cnt = 0;
		int printCnt = 0;
		
		System.out.print("<");
		while(tmp != null) {
			if(k==1) {
				printCnt++;
				if(printCnt > n) break;
				System.out.print(tmp.val);
				if(printCnt < n) {
					System.out.print(", ");
				}
				tmp = tmp.next;
				
			}
			
			else {
					cnt++;
					if(cnt == k) {
						cnt = 0;
						res = l.deleteNode(sub,tmp);
						sub = sub.next;
						tmp = sub;
						System.out.print(res);
						printCnt++;
						if(printCnt<n) {
							System.out.print(", ");
						}
					}
					else {
						sub = tmp;
						tmp  = tmp.next;
					}
			}
		}
		System.out.print(">");
		

	}

}