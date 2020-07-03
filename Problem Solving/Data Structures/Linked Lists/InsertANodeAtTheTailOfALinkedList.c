SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) 
{
    SinglyLinkedListNode* temp=(SinglyLinkedListNode*) malloc(sizeof(SinglyLinkedListNode));
    temp->data=data;
    temp->next=NULL;
    SinglyLinkedListNode* last=head;
    if(head==NULL)
    head=temp;
    else
    {
        while(last->next!=NULL)
        last=last->next;

        last->next=temp;

    }
 return head;

}
