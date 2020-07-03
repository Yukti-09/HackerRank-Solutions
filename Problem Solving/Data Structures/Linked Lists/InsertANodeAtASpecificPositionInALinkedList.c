SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* head, int data, int position) 
{
    int x=0;
    SinglyLinkedListNode* last=head;
SinglyLinkedListNode* temp=(SinglyLinkedListNode*)malloc(sizeof(SinglyLinkedListNode));
temp->data=data;
temp->next=NULL;
if(head==NULL)
{
    head=temp;
}

else
{
    while(x!=position-1)
    {
        last=last->next;
        x++;
    }
    
    
        temp->next=last->next;
        last->next=temp;
    
    
}
return head;

}
