#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list contains a cycle.
 * @list: A pointer to the head of the linked list.
 * Return: 1 if a cycle is found, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_ptr = list;
	listint_t *slow_ptr = list;

	if (!list)
		return (0);

	while (1)
	{
		if (fast_ptr->next != NULL && fast_ptr->next->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			slow_ptr = slow_ptr->next;

			if (fast_ptr == slow_ptr)/*condition to find cycle*/
				return (1);
		}
		else
			return (0);
	}
}
