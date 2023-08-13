#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	unsigned int i = 0, len_l = 0;
	int *l1;
	listint_t *l2 = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (l2)
	{
		l2 = l2->next;
		len_l++; }
	if (len_l == 1)
		return (1);
	l2 = *head;
	l1 = malloc(sizeof(int) * len_l);
	if (!l1)
		return (0);
	while (l2)
	{
		l1[i++] = l2->n;
		l2 = l2->next; }
	for (i = 0; i < (len_l / 2) + 1; i++)
	{
		if (l1[i] != l1[len_l - i - 1])
		{
			free(l1);
			return (0); }}
	free(l1);
	return (1);
}
