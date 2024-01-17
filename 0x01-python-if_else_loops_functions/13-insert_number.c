#include "lists.h"

/**
 * insert_node - Add new node at a particular position.
 * @head: head of a linked list.
 * @number: index of where the new node is.
 * Return: address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *h;
	listint_t *head_prev;

	h = *head;
	current = malloc(sizeof(listint_t));

	if (current == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		head_prev = h;
		h = h->next;
	}

	current->n = number;

	if (*head == NULL)
	{
		current->next = NULL;
		*head = current;
	}
	else
	{
		current->next = h;
		if (h == *head)
			*head = current;
		else
			head_prev->next = current;
	}

	return (current);
}
