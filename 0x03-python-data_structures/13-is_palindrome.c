#include "lists.h"

/**
 * is_palindrome - Determine if singly linked list is a palindrome.
 * @head: Pointer to the head of the singly linked list.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	unsigned int size = 0, i;
	int data[10240];

	if (head == NULL)
		return (0); /* Non-existing list is not a palindrome */

	if (*head == NULL)
		return (1); /* An empty list is a palindrome */

	/* Find the size of the linked list and store node data in an array */
	while (current)
	{
		data[size++] = current->n;
		current = current->next;
	}

	/* Check if the list is a palindrome by comparing data elements */
	for (i = 0; i < size / 2; i++)
	{
		if (data[i] != data[size - i - 1])
			return (0); /* Not a palindrome */
	}

	return (1); /* It's a palindrome */
}

