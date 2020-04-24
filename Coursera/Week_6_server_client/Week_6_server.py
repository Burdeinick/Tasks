import asyncio
import time


dic = {}


def run_server(host, port):
    """ """

    loop = asyncio.get_event_loop()
    coro = loop.create_server
    (ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    """ """

    def connection_made(self, transport):
        self.transport = transport

    def _send(self, data_send):
        self.transport.write(data_send.encode())

    def _read(self, data_read):
        return data_read.decode()

    def take_put(self, payload):
        """ """

        try:
            payload = payload.strip()
            metric, value, timestamp = payload.split()

            if metric not in dic:
                dic[metric] = [(float(value), int(timestamp))]

            elif metric in dic:
                for tup_val in dic[metric]:
                    if int(timestamp) == int(tup_val[1]):
                        del_tup = dic[metric].index(tup_val)
                        del dic[metric][del_tup]
                dic[metric].append((float(value), int(timestamp)))

        except ValueError:
            return 'error\nwrong command\n\n'

        except TypeError:
            return 'error\nwrong command\n\n'

    def take_get(self, payload):
        """ """

        get_str = 'ok'
        payload = payload.strip()
        test_len = payload.split()
        if len(test_len) > 1:
            return 'error\nwrong command\n\n'

        if payload == '*':
            if not dic:
                get_str += '\n\n'
                return get_str

            elif dic:
                for keys in dic:
                    for values in dic[keys]:
                        get_str += f'\n{keys}'
                        for lines in values:
                            get_str += f' {lines}'
                get_str += '\n\n'
                return get_str

        if payload in dic:
            for values in dic[payload]:
                get_str += f'\n{payload}'
                for line in values:
                    get_str += f' {line}'
            get_str += '\n\n'
            return get_str

        if not payload:
            return 'error\nwrong command\n\n'

        if payload not in dic:
            get_str += '\n\n'
            return get_str
        else:
            return 'error\nwrong command\n\n'

    def data_received(self, data):
        """ This method realizes read of the data  of the socket """

        data_of_client = self._read(data)

        try:
            if data_of_client:
                status, payload = data_of_client.split(" ", 1)

            # PUT
            if status == 'put':

                if self.take_put(payload) is None:
                    self._send('ok\n\n')
                    print('self.take_put(payload) is None: = ', 'None')
                else:
                    self._send(self.take_put(payload))
                    print('self.take_put(payload)')

            # GET
            elif status == 'get':
                self._send(self.take_get(payload))

            # WRONG COMMAND
            else:
                self._send('error\nwrong command\n\n')

        except Exception:
            self._send('error\nwrong command\n\n')

# run_server("127.0.0.1", 8888)
