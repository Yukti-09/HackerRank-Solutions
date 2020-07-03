struct node* insert( struct node* root, int data ) 
{
		struct node * temp=(struct node *)malloc(sizeof(struct node));
        temp->data=data;
        temp->left=NULL;
        temp->right=NULL;
        if(root==NULL)
        return temp;
        else if(data>root->data)
        root->right=insert(root->right,data);
        else 
        root->left=insert(root->left,data);
        return root;

	
}

