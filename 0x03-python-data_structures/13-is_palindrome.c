#include "lists.h"

/**
 * is_palindrome - function that determine if singly linked list is palindrome.
 * @head: Pointer to head of singly linked list.
 * Return: 0 if not palindrome Otherwise 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr_node = *head;
	unsigned int size = 0, i = 0;
	int data[10240];

	if (head == NULL) /* non existing list is not palindrome*/
		return (0);

	if (*head == NULL) /* exist but empty list is palindrome */
		return (1);

	while (curr_node) /* find the size of linked list */
	{
		curr_node = curr_node->next;
		size += 1;
	}
	if (size == 1) /* single node in list is palindrome */
		return (1);

	curr_node = *head;
	while (curr_node) /* pull node data into array to compare */
	{
		data[i++] = curr_node->n;
		curr_node = curr_node->next;
	}

	for (i = 0; i <= (size / 2); i++)
	{
		if (data[i] != data[size - i - 1])
			return (0);
	}
	return (1);
}
