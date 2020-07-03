SinglyLinkedListNode* deleteNode(SinglyLinkedListNode* head, int position) 
{
int x=0;
SinglyLinkedListNode* curr;
curr=head;
SinglyLinkedListNode* prev;
prev=NULL;
SinglyLinkedListNode* temp;
if(curr->next==NULL)
{
    head=NULL;
}
else
{
    if(position==0)
    {
        temp=head;
        head=head->next;
        free(temp);
    }
    else{
while(x!=position)
{
    prev=curr;
    curr=curr->next;
    x++;
}
temp=curr;
prev->next=curr->next;
free(temp);

}
}
return head;
}
