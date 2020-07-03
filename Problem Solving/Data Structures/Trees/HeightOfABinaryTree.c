int getHeight(struct node* root) {
   if(root==NULL)
   return -1;
   
   else
   {
       int l,r;
       l=getHeight(root->left);
       r=getHeight(root->right);
       if(l>r)
       return (l+1);
       else 
       return (r+1);
   }
}

