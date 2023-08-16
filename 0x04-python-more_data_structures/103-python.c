#include "Python.h"
#include "listobject.h"
#include "object.h"
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	int len = 0, a;
	char *s;
	PyBytesObject *py_c = (PyBytesObject *) p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py_c))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	else
	{
		len = PyBytes_Size(p);
		if ((len + 1) >= 10)
			a = 10;
		printf("  size: %d\n", len);
		printf("  trying string: %s\n", py_c->ob_sval);
		s = py_c->ob_sval;
		printf("  first %d bytes: ", a);
		while (a--)
			printf(" %.2x", (unsigned char) *s++);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
void print_python_list(PyObject *p)
{
	int i, len = 0;
	PyListObject *py_c = (PyListObject *) p;
	PyObject *it;

	len = PyList_GET_SIZE(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lld\n", (long long) len);
	printf("[*] Allocated = %lld\n", (long long) py_c->allocated);
	for (i = 0; i < (long long) len; ++i)
	{
		it = PyList_GET_ITEM(p, i);
		printf("Element %lld: %s\n", i, it->ob_type->tp_name);
		if (PyBytes_Check(it))
			print_python_bytes(it);
	}
}
