/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package doubly;

/**
 *
 * @author multimedia
 */

public class Doublelinkedlist { 
    Node head ;
     class Node {
         int data;
         Node prev;
         Node next;
         
         Node(int d) {data = d;}
     }
     public void push(int data){
         Node newnode = new Node(data);
         
         newnode.next = head;
         newnode.prev = null;
         
         if(head != null)
             head.prev = newnode;
         head = newnode;
         
                
     }
     public void InsertAfter(Node prev_node, int data){
         if(prev_node == null){
             System.out.print("the given prev_node cannot be null");
             return;
            }
         
         Node newnode = new Node(data);
         newnode.next = prev_node.next;
         prev_node.next = newnode;
         newnode.prev = prev_node;
         
         if (newnode.next != null)
             newnode.next.prev = newnode;     
        
     }
     public void append(int data){
         Node newnode = new Node(data);
         Node last = head;
         newnode.next = null;
         if (head == null){
             newnode.prev = null;
             head = newnode;
             return;
         }
        while(last.next != null)
            last = last.next;
        last.next=newnode;
        newnode.prev = last;                               
                 
     }
     public void printlist(Node node){
         Node last = null;
         System.out.println("traversal in forward :");
         while (node != null){
             System.out.println(node.data+" ");
             last = node;
             node = node.next;
                     
         }
          System.out.println();
           System.out.println("traversal in reverse:");;
           while (last != null){
                System.out.println(last.data+" ");
                last = last.prev;
           }
         
         
                 
     }

       

public static void main(String[] args){
    Doublelinkedlist dll = new Doublelinkedlist();
    dll.append(3);
    dll.push(2);
    dll.push(8);
    dll.append(7);
    dll.InsertAfter(dll.head.next ,2);
    
    System.out.println("here we go :");
    dll.printlist(dll.head);
    
    

}
}