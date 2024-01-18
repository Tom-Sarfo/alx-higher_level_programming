#include "lists.h"

/**
 * check_cycle - checks for cycle in a singly linked list
 * @list: pointer to list
 * Return: if 0 no cycle,
 * 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr2;
	listint_t *prev;

	ptr2 = list;
	prev = list;
	while (list && ptr2 && ptr2->next)
	{
		list = list->next;
		ptr2 = ptr2->next->next;

		if (list == ptr2)
		{
			list = prev;
			prev =  ptr2;
			while (1)
			{
				ptr2 = prev;
				while (ptr2->next != list && ptr2->next != prev)
				{
					ptr2 = ptr2->next;
				}
				if (ptr2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
