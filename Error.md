```java
2017-09-26 13:34:05,317 | ERROR | g-fcrepo-create] | FcrepoIndexer                    | 114 - ca.islandora.alpaca.islandora-indexing-fcrepo - 0.3.1.SNAPSHOT | org.apache.camel.http.common.HttpOperationFa$
        at org.apache.camel.component.http4.HttpProducer.populateHttpOperationFailedException(HttpProducer.java:312)
        at org.apache.camel.component.http4.HttpProducer.process(HttpProducer.java:207)
        at org.apache.camel.util.AsyncProcessorConverterHelper$ProcessorToAsyncProcessorBridge.process(AsyncProcessorConverterHelper.java:61)
        at org.apache.camel.processor.SendDynamicProcessor$1.doInAsyncProducer(SendDynamicProcessor.java:124)
        at org.apache.camel.impl.ProducerCache.doInAsyncProducer(ProducerCache.java:436)
        at org.apache.camel.processor.SendDynamicProcessor.process(SendDynamicProcessor.java:119)
        at org.apache.camel.management.InstrumentationProcessor.process(InstrumentationProcessor.java:77)
        at org.apache.camel.processor.RedeliveryErrorHandler.process(RedeliveryErrorHandler.java:541)
        at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:198)
        at org.apache.camel.processor.Pipeline.process(Pipeline.java:120)
        at org.apache.camel.processor.Pipeline.process(Pipeline.java:83)
        at org.apache.camel.processor.FilterProcessor.process(FilterProcessor.java:57)
        at org.apache.camel.management.InstrumentationProcessor.process(InstrumentationProcessor.java:77)
        at org.apache.camel.processor.RedeliveryErrorHandler.process(RedeliveryErrorHandler.java:541)
        at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:198)
        at org.apache.camel.processor.Pipeline.process(Pipeline.java:120)
        at org.apache.camel.processor.Pipeline.process(Pipeline.java:83)
        at org.apache.camel.processor.CamelInternalProcessor.process(CamelInternalProcessor.java:198)
        at org.apache.camel.processor.DelegateAsyncProcessor.process(DelegateAsyncProcessor.java:97)
        at org.apache.camel.component.jms.EndpointMessageListener.onMessage(EndpointMessageListener.java:112)
        at org.springframework.jms.listener.AbstractMessageListenerContainer.doInvokeListener(AbstractMessageListenerContainer.java:721)
        at org.springframework.jms.listener.AbstractMessageListenerContainer.invokeListener(AbstractMessageListenerContainer.java:681)
        at org.springframework.jms.listener.AbstractMessageListenerContainer.doExecuteListener(AbstractMessageListenerContainer.java:651)
        at org.springframework.jms.listener.AbstractPollingMessageListenerContainer.doReceiveAndExecute(AbstractPollingMessageListenerContainer.java:313)
        at org.springframework.jms.listener.AbstractPollingMessageListenerContainer.receiveAndExecute(AbstractPollingMessageListenerContainer.java:251)
        at org.springframework.jms.listener.DefaultMessageListenerContainer$AsyncMessageListenerInvoker.invokeListener(DefaultMessageListenerContainer.java:1164)
        at org.springframework.jms.listener.DefaultMessageListenerContainer$AsyncMessageListenerInvoker.executeOngoingLoop(DefaultMessageListenerContainer.java:1156)
        at org.springframework.jms.listener.DefaultMessageListenerContainer$AsyncMessageListenerInvoker.run(DefaultMessageListenerContainer.java:1053)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)
        Suppressed: org.apache.camel.http.common.HttpOperationFailedException: HTTP operation failed invoking http://localhost:8000/milliner/rdf/8000/node/4 with statusCode: 404
                ... 31 more
                Suppressed: org.apache.camel.http.common.HttpOperationFailedException: HTTP operation failed invoking http://localhost:8000/milliner/rdf/8000/node/4 with statusCode: 404
                        ... 31 more
                        Suppressed: org.apache.camel.http.common.HttpOperationFailedException: HTTP operation failed invoking http://localhost:8000/milliner/rdf/8000/node/4 with statusCode: 404
                                ... 31 more
                                Suppressed: org.apache.camel.http.common.HttpOperationFailedException: HTTP operation failed invoking http://localhost:8000/milliner/rdf/8000/node/4 with statusCode: 404
                                        ... 31 more
                                        Suppressed: org.apache.camel.http.common.HttpOperationFailedException: HTTP operation failed invoking http://localhost:8000/milliner/rdf/8000/node/4 with statusCod$
                                                ... 31 more

```
