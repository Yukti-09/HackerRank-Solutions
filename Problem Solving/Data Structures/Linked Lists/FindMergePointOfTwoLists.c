int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) 
{
    SinglyLinkedListNode* one=head1;
    SinglyLinkedListNode* two=head2;
    for (;one; one = one->next)
    {
        SinglyLinkedListNode* two=head2;
        for (; two; two = two->next)
        {
            if(one == two) return one->data;
        }
    }
    
   return 0;
    
}

