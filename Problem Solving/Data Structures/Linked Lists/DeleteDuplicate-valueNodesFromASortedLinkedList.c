SinglyLinkedListNode* removeDuplicates(SinglyLinkedListNode* head) 
{
    if(head->next==NULL)
        return head;
    else
    {
        SinglyLinkedListNode* prev=head;
        SinglyLinkedListNode* curr=head->next;
        SinglyLinkedListNode* temp;
        while(curr!=NULL)
        {
            if(prev->data==curr->data)
            {
                temp=curr;
            prev->next=curr->next;
            free(temp);
            curr=prev->next;
            }
            else 
            {
                prev=curr;
                curr=curr->next;
            }
            
        }
        return head;
        
    }
}
    

